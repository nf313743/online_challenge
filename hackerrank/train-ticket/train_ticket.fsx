let smallBerthers n =
    let myList = ["UB";"LB"; "MB"]
    myList.[(n % 3)]

let berther n =
    match n % 8 with
    | 0 -> "SUB"
    | 7 -> "SLB"
    | x -> smallBerthers x


System.Console.ReadLine() 
|> int
|> berther
|> printfn "%s"
