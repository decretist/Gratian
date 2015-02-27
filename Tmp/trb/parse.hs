{-# LANGUAGE OverloadedStrings #-}
import Control.Applicative ((*>), (<$>), (<*), (<*>), (<|>))
import Data.Attoparsec.ByteString.Char8
import qualified Data.ByteString as B
import Data.List (delete)
import Data.List.Split (splitWhen)
import Data.Text (pack, strip, unpack)
import System.Environment (getArgs)
import Text.Printf

data Element = Tag String String | Header String | Plain String
  deriving (Eq, Ord, Show)

-- Parsing
unspecial = satisfy $ notInClass "-+<>"

plain = Plain <$> many1' unspecial
header = Header <$> (char '-' *> many' unspecial <* char '+')
tag = Tag
  <$> (char '<' *> many1' (notChar ' '))
  <*> (skipSpace *> many1' (notChar '>') <* char '>')

element = tag <|> header <|> plain

-- Post-parsing
sectionBreak (Tag "2" _) = True
sectionBreak _ = False

toText (Plain s) = s
toText _ = " "

replaceLineBreaks '\n' = ' '
replaceLineBreaks x = x

format :: Int -> String -> String
format i s = printf "%03d _ %s" i s

main = do
  path <- head <$> getArgs
  Right res <- parseOnly (many1 element) <$> B.readFile path
  mapM_ (\(i, s) -> putStrLn $ format i s)
    $  zip [1..] 
    $  filter (not . null . unpack . strip . pack)
    $  (map replaceLineBreaks . concatMap toText)
   <$> splitWhen sectionBreak res

