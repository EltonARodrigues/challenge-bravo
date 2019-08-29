package model

import (
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
	"log"
	"fmt"
)

type Currency struct {
	gorm.Model
	Name	  string  `json:"name"`
	Usd_value float64 `json:"usd_value"`

}

// DBMigrate will create and migrate the tables, and then make the some relationships if necessary
func dbMigrate(db *gorm.DB) *gorm.DB {
	db.AutoMigrate(&Currency{})
	return db
}

func InitializeDB() *gorm.DB {
	dbURI := fmt.Sprintf("%s:%s@/%s?charset=%s&parseTime=True",
		"root",
		"elton56261",
		"currency",
		"utf8")
 
	db, err := gorm.Open("mysql", dbURI)
	if err != nil {
		log.Print(dbURI)
		log.Fatal("Could not connect database %s")
	}

	return dbMigrate(db)

}