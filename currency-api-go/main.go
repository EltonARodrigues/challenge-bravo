package main

import (
	"fmt"

	//"github.com/EltonARodrigues/currency-api-go/app/config"
	"github.com/EltonARodrigues/currency-api-go/app"
)

func main() {
	var address string
	//config := *config.GetConf()

	/*for _, c := range config.App {
		address = fmt.Sprintf(":%s",c.Address)
	}*/
	address = ":3000"
	fmt.Println(address)
	app.Initialize()
	app.Run(address)
}