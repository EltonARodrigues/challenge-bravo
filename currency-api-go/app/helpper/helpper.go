package helpper

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"
	"fmt"
)

type Response struct {
    Rates    interface{}    `json:"rates"`
    Base string `json:"base"`
    Date string `json:"date"`
}

func Import_all(key string) *Response {
	var url string
	if key == "latest" {
		url = "https://api.exchangeratesapi.io/latest"
	}  else {
		url = fmt.Sprintf("https://api.exchangeratesapi.io/latest/?symbols=%s&base=USD", key)
	}

	response, err := http.Get(url)
    if err != nil {
        log.Print(err.Error())
    }

    responseData, err := ioutil.ReadAll(response.Body)
    if err != nil {
        log.Fatal(err)
	}
	var responseObject Response
	json.Unmarshal(responseData, &responseObject)
	return &responseObject
}