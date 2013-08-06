object Main {
  def main(args : Array[String]){
    lazy val fib: Stream[Int] = 0 #:: 1 #:: fib.zip(fib.tail).map( t => t._1 + t._2 )
    println(fib.takeWhile(_ <= 4000000).filter(_ % 2 == 0).sum)
  }
}
