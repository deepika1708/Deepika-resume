d = open("Deepika.html","w")
a = """<html>
 <head>
<title>RESUME</title>

<style type="text/css">
    table {
        font-size: 20px;
    }
    #heading{
        font-size: 20px;
        }
</style>
</head>
<body>
<div >
  <center><h1><u>MY RESUME</u></h1></center>  
<h3> Deepika Sanodiya</h3>
<p > deepusuno@gmail.com</p>
<p>DOB: 17 Aug 2000</p>
<p>Narayan Nagar Bhopal</p
<p>Contact No.: 9165261575</p>
 
  <h2><u>CAREER OBJECTIVE</u></h2>
  <p>To succeed in an environment of growth 
     and excellence in computer science and 
     earn a job which provide me job satisfaction
     and self development and help me in achieving
      personal as well as organization goals.</p>
            <h2><u>EDUCATION </u></h2>
            <table border="1">
                <tr >
                    <th>Qualification</th>
                    <th>Institute</th>
                    <th>Percentage / Grades</th>
                    <th>Year</th>
                </tr>
                <tr>
                    <td>10th</td>
                    <td>Modern Higher Secondary<br> school seoni</td>
                    <td>77%</td>
                    <td>2016</td>
                </tr>
                <tr>
                    <td>12th</td>
                    <td>Modern Higher Secondary<br> school seoni</td>
                    <td>82.8%</td>
                    <td>2018</td>
                </tr>
                <tr>
                    <td>1st Sem</td>
                    <td>Barkatullah University Institute<br> Of Technology Bhopal</td>
                    <td>8.56 SGPA</td>
                    <td>2019</td>
                </tr>
                <tr>
                    <td>2nd Sem</td>
                    <td>Barkatullah University Institute<br> Of Technology Bhopal</td>
                    <td>8.16 SGPA</td>
                    <td>2019</td>
                </tr>
                
            </table>
        </div>
         <h2><u>HOBBIES</u></h2>
          <p>Reading books,</p>
           <p>Dancing and Singing.</p>
          <h2><u>LANGUAGES</u></h2>
           <p>Hindi</p>
           <p>English.</p> 
          <h2><u>SKILLS</u></h2>
           <p>C,C++ and HTML.</p>
         <h2><u>WORK  EXPERIENCE</u></h2>
        <p>Fresher.</p>

</body>
</html>"""
d.write(a)
d.close()
