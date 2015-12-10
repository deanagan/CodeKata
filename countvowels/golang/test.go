
package main

import "fmt"
import "strings"

func Filter(vs []string, f func(string) bool) []string {
    vsf := make([]string, 0)
    for _, v := range vs {
        if f(v) {
            vsf = append(vsf, v)
        }
    }
    return vsf
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

