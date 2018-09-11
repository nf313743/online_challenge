let input1 = ["c"; "d"; "a"; "b"]
let input2 = ["a"; "b"; "c"; "d"]

let evenList = 
    input1 
    |> List.mapi(fun i el -> i , el ) 
    |> List.filter(fun (i, _) -> i % 2 = 0)
    |> List.map (fun (_, el) -> el)
    |>
    set

let oddList = 
    input1 
    |> List.mapi(fun i el -> i , el ) 
    |> List.filter(fun (i, _) -> i % 2 <> 0)
    |> List.map (fun (_, el) -> el)
    |>
    set

printf "%A" (oddList)


printf "%A" (evenList = oddList)