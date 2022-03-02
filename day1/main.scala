object Hello {

    def lowercase(text: String) = text.toLowerCase

    def main(args: Array[String]) = {
        val testText = "Ala Ma KoTa"
        println(s"lowercase($testText) = ${lowercase(testText)}")
    }
}