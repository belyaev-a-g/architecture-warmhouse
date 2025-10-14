package services

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

// TemperatureService handles fetching temperature data from external API
type TemperatureService struct {
	BaseURL    string
	HTTPClient *http.Client
}

// TemperatureResponse represents the response from the temperature API
type TemperatureResponse struct {
	Value       float64   `json:"value"`
	Unit        string    `json:"unit"`
	Timestamp   time.Time `json:"timestamp"`
	Location    string    `json:"location"`
	Status      string    `json:"status"`
	SensorID    string    `json:"sensor_id"`
	SensorType  string    `json:"sensor_type"`
	Description string    `json:"description"`
}

// NewTemperatureService creates a new temperature service
func NewTemperatureService(baseURL string) *TemperatureService {
	return &TemperatureService{
		BaseURL: baseURL,
		HTTPClient: &http.Client{
			Timeout: 10 * time.Second,
		},
	}
}

// GetTemperature fetches temperature data for a specific location
func (s *TemperatureService) GetTemperature(location string) (*TemperatureResponse, error) {
	url := fmt.Sprintf("%s/temperature?location=%s", s.BaseURL, location)
        println("location query = %s", url)

	resp, err := s.HTTPClient.Get(url)


	if err != nil {
		return nil, fmt.Errorf("error fetching temperature data: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("unexpected status code: %d", resp.StatusCode)
	}

        var output string
        if err2 := json.NewDecoder(resp.Body).Decode(&output); err2 != nil {
		return nil, fmt.Errorf("ERR2 error decoding temperature response: %w", err2)
        }
 

	var temperatureResp TemperatureResponse
	if err := json.NewDecoder(resp.Body).Decode(&temperatureResp); err != nil {
		return nil, fmt.Errorf("error decoding temperature response: %w", err)
	}

	return &temperatureResp, nil
}

// GetTemperatureByID fetches temperature data for a specific sensor ID
func (s *TemperatureService) GetTemperatureByID(sensorID string) (*TemperatureResponse, error) {
	url := fmt.Sprintf("%s/temperature?sensor_id=%s", s.BaseURL, sensorID)

	resp, err := s.HTTPClient.Get(url)

/*
        println("sensor query: body = %s", resp.Body)

        bbody := resp.Body
        // Читаем тело ответа
        body, err := io.ReadAll(bbody)
        if err != nil {
            fmt.Println("Ошибка чтения тела: %v", err)
        }

        fmt.Println("=== Response Body ===")
        fmt.Println(string(body))

        // Также выводим метаинформацию
        fmt.Printf("\n=== Response Info ===\n")
        fmt.Printf("Status: %s\n", resp.Status)
        fmt.Printf("Content-Type: %s\n", resp.Header.Get("Content-Type"))
        fmt.Printf("Content-Length: %d\n", resp.ContentLength)

        //var t_str = "2025-10-14T13:04:51.614023"
        var t_str = "2025-10-14T13:04:51Z"
        fmt.Printf("My time string: %s\n", t_str)
       
        t, err3 := time.Parse(time.RFC3339, t_str)
       if err3 != nil {
           fmt.Println("Parse error")
       }
       fmt.Println(t)
*/

	if err != nil {
		return nil, fmt.Errorf("error fetching temperature data: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("unexpected status code: %d", resp.StatusCode)
	}

	var temperatureResp TemperatureResponse
	if err := json.NewDecoder(resp.Body).Decode(&temperatureResp); err != nil {
		return nil, fmt.Errorf("error decoding temperature response: %w", err)
	}

	return &temperatureResp, nil
}

