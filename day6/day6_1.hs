-- This just wraps the getLine funtion but you could operate over the input before return the final result
processInput :: IO String
processInput = do
    name <- getLine
    return (doit $ name)

gi :: [String] -> (Int, Int, Int)
gi x = (read (x !! 0), read (x !! 1), read (x !! 2))

doit :: String -> String
doit x = do
    gis <- gi (words $ x)
    gis !! 0

-- This is our main loop, it handles when to exit
loop :: IO ()
loop = do
    line <- processInput
    putStrLn line
    case line of
        "quit"    -> return ()
        otherwise -> loop

-- main is the program entry point
main :: IO ()
main = do
    putStrLn "Welcome to the haskel input example"
    loop