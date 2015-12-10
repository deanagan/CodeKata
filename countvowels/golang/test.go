
package main

import "fmt"
import "strings"

func Filter(vs []string, f func(string) bool) []string {
    splittedstrings := make([]string, 0)
    for _, ch := range vs {
        if f(ch) {
            splittedstrings = append(splittedstrings, ch)
        }
    }
    return splittedstrings
}

func countvowels(inputStr string) int {
    s := Filter ( strings.Split(inputStr, ""), func (str string) bool {
        return strings.Contains("aeiouAEIOU", str)
    })
   

    return len(s)
}

func main() {
    count := countvowels("hello")
    fmt.Println("The number of vowels in hello is ", count)

}

