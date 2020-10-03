//Binary Search in Golang

package main
import "fmt"
func binarySearch(needle int, haystack[]int) bool {
    low := 0
    high := len(haystack) - 1
    
    for low<=high{
        median:=(low+high) / 2
        
        if haystack[median] < needle {
            low = median + 1 
        }else{
            high = median - 1 
        }
    }
    
    if low == len(haystack) || haystack[low] != needle {
        return false
    }
    
    return true
}

func main(){
    
    length := 0
    fmt.Println("Enter the number of inputs: ")
    fmt.Scanln(&length)
    
    fmt.Println("Enter the inputs: ")
    
    items := make([]int, length)
    for i := 0; i < length; i++ {
        fmt.Scanln(&items[i])
    }
    
    number := 0
    fmt.Println("Enter the number to be searched for: ")
    fmt.Scanln(&number)
    
    //function calling
    fmt.Println(binarySearch(number, items))
}
