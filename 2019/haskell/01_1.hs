import System.IO

fuel :: [String] -> Int
fuel = foldr (+) 0 . map (\x -> (read x `div` 3) - 2)

main :: IO ()
main = do
    y <- readFile "2019/01.txt"
    print (fuel (lines y))

-- maybe there is a better way than printing