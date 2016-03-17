package main

import (
  "bufio"
  "fmt"
  "net"
  "strconv"
)


func fib(n int) int {
    if n <= 2 {
        return 1
    }
    return fib(n-1)+fib(n-2)
}


func fibHandler(conn net.Conn) {
    for {
        message, err := bufio.NewReader(conn).ReadString('\n')
        if err != nil {
            break
        }
        // strip out \n from the bufio Reader
        n, _ := strconv.Atoi(message[:len(message)-1])
        result := fib(n)
        resp := []byte(strconv.Itoa(result)+ "\n")
        conn.Write(resp)
    }
    conn.Close()
    fmt.Println("Closed")
}


func main() {
  ln, _ := net.Listen("tcp4", ":25000")
  for {
    conn, _ := ln.Accept()
    go fibHandler(conn)
  }
}
