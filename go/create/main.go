package main

import (
	"database/sql"
	"fmt"

	_ "github.com/mattn/go-sqlite3"
)

func main() {
	conn, err := sql.Open("sqlite3", "./test.db")
	if err != nil {
		panic(err)
	}
	defer conn.Close()

	_, err = conn.Exec(`
	CREATE TABLE IF NOT EXISTS users(
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		username VARCHAR(150) NOT NULL,
		password VARCHAR(150) NOT NULL,
		is_addmin BOOLEAN DEFAULT TRUE
	)
	`)
	if err != nil {
		panic(err)
	}
	_, err = conn.Exec(`
		CREATE TABLE IF NOT EXISTS category(
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			name VARCHAR(150) NOT NULL,
			created_at TIMESTAMP,
			updated_at TIMESTAMP
		)
	`)
	if err != nil {
		panic(err)
	}
	_, err = conn.Exec(`
		CREATE TABLE IF NOT EXISTS course (
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			name VARCHAR(150) NOT NULL,
			body TEXT NOT NULL,
			is_active BOOLEAN DEFAULT TRUE,
			created_at TIMESTAMP,
			updated_at TIMESTAMP
		)
	`)
	if err != nil {
		panic(err)
	}
	_, err = conn.Exec(`
		CREATE TABLE IF NOT EXISTS user_course(
			user_id INTEGER,
			course_id INTEGER,
			PRIMARY KEY(user_id, course_id),
			FOREIGN KEY(user_id) REFERENCES users(id),
			FOREIGN KEY(course_id) REFERENCES course(id)
		)
	`)
	if err != nil {
		panic(err)
	}

	fmt.Println("Go running>")
}
