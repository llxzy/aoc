import System.IO 

revCount :: Int -> Int
revCount n = if n > 0 then n + revCount ( (n `div` 3) - 2) else 0

fuelCount :: [String] -> Int
fuelCount = foldr (+) 0 . map (revCount . (\x -> x `div` 3 - 2) . read) 

main :: IO ()
main = do
    y <- readFile "2019/01.txt"
    print (fuelCount (lines y))