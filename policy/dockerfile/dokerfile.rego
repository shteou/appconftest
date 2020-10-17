package main

deny[msg] {
    input[i].Cmd == "from"
    val := split(input[i].Value[0], ":")
    contains(lower(val[1]), "latest")
    msg = sprintf("Line %d: do not use 'latest' tag for base images", [i])
}

deny[msg] {
    input[i].Cmd == "from"
    not contains(input[i].Value[0], ":")
    msg = sprintf("Line %d: does not specify a version, implicit 'latest'", [i])
}

