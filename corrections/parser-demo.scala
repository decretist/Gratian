sealed trait Element
case class Tag(name: String, attr: String) extends Element
case class Header(text: String) extends Element
case class Plain(text: String) extends Element

import scala.util.parsing.combinator._

object parse extends RegexParsers {
  override def skipWhitespace = false
  def tag: Parser[Tag] = ("<" ~> "\\S+".r <~ "\\s".r) ~ "[^\\s>]+".r <~ ">" ^^ {
    case name ~ attr => Tag(name, attr)
  }
  def header: Parser[Header] = "\\-".r ~> "[^+]*".r <~ "+" ^^ (Header(_))
  def plain: Parser[Plain] = "[^<>\\-\\+]+".r ^^ (Plain(_))
  def elements: Parser[List[Element]] = rep(tag | header | plain)
  def apply(s: String) = parseAll(elements, s)
}

val text = io.Source.fromFile(
  "./edF.txt"
).getLines.take(10000).mkString(" ")

parse(text).get foreach println
