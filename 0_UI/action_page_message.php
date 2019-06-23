 <?php
        $pathFile = "/var/fpwork/hcostina/proiect/trunk/mesaje.txt";
        $File = fopen($pathFile, 'a') or die("Unable to open file!");
        fwrite($File, $_GET["mesajnou"] . "\n");
        fclose($File);
 ?>

<html>
<title>Control</title>
<body>
<p>Mesaj trimis</p>
<p>
<form method="get" action="/index.php">
	<button type="submit">Inapoi</button>
</form>
</p>
</body>
</html>

