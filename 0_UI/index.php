<html>
 <head>

  <title>Control</title>
 </head>
 <body>

 <?php echo '<p>Salut,</p>'; ?>
 <p>Temperatura actuala este: 
 <?php
    $myFile = "/var/fpwork/hcostina/proiect/trunk/temperatura.txt";
    $fh = fopen($myFile, 'r');
    $theData = fread($fh, 3);
    fclose($fh);
    echo $theData;
    ?> *C<br>
    Temperatura pentru controlul automat este:
 <?php
    $myFile = "/var/fpwork/hcostina/proiect/trunk/control.txt";
    $fh = fopen($myFile, 'r');
    $theData = fread($fh, 3);
    fclose($fh);
    echo $theData;
    ?> *C</p>

 <p>	<form action="/action_page.php">
  		Temperatura dorita:<br>
 		<input type="text" name="temper" value="">
  		<br>
 	 <input type="submit" value="Trimite">
	</form>
 </p>
 <p>    <form action="/action_page_message.php">
               Mesaj nou:<br>
               <input type="text" name="mesajnou" value="">
               <br>
        <input type="submit" value="Trimite">
       </form>
</p>
 </body>
</html>
