package main

import (
    "encoding/json"
    "fmt"
    "log"
    "net/http"
    "time"
)

func main() {
    url := "http://temperature-api:5000/temperature?sensor_id=2"
    //url := "http://localhost:5000/temperature?sensor_id=2"
    fmt.Println("API URL: %s", url)

    var resp *http.Response
    var err error
    
    // Пытаемся выполнить запрос несколько раз
    for i := 0; i < 33333; i++ {
        resp, err = http.Get(url)
        if err == nil && resp.StatusCode == http.StatusOK {
            break
        }
        
        if err != nil {
            log.Printf("Попытка %d: Ошибка: %v", i+1, err)
        } else {
            log.Printf("Попытка %d: Неверный статус: %s", i+1, resp.Status)
            resp.Body.Close()
        }
        
        time.Sleep(2 * time.Second)
    }
    
    if err != nil {
        log.Fatalf("Не удалось выполнить запрос после 3 попыток: %v", err)
    }
    defer resp.Body.Close()

    // Просто выводим сырой ответ
    var result map[string]interface{}
    json.NewDecoder(resp.Body).Decode(&result)
    
    fmt.Println("📡 Ответ от API:")
    for key, value := range result {
        fmt.Printf("  %s: %v\n", key, value)
    }
}
