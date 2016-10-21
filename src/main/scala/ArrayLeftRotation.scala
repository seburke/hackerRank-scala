
object ArrayLeftRotation {

    def shiftLeft(a: Array[Int], n: Int, k: Int) : Array[Int] = {
        val newK = n - k%n
        reverse(a, 0, n-1)
        reverse(a,0, newK-1)
        reverse(a,newK, n-1)
    }

    def reverse(a: Array[Int], s: Int, f: Int) : Array[Int] = {
        var l = s
        var r = f
        while (l < r) {
            val temp = a(l)
            a(l) = a(r)
            a(r) = temp
            l += 1
            r -= 1
        }
        return a
    }

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var n = sc.nextInt()
        var k = sc.nextInt()
        var a = new Array[Int](n)
        for(a_i <- 0 to n-1) {
            a(a_i) = sc.nextInt()
        }
        shiftLeft(a,20,10)
        println(a.mkString(" "))

    }
}
