<%@ page language="java" contentType="text/html; charset=US-ASCII"
    pageEncoding="US-ASCII"%>
    <%@page import="java.io.*" %>
    <%@page import="java.net.*" %>
    <%@page import="java.lang.*" %>
    <%@page import="java.lang.*" %>
    <%@page import="project56.test" %>
    <%@ taglib prefix="c" uri="http://java.sun.com/jstl/core" %>
	<%@ taglib prefix="x" uri="http://java.sun.com/jstl/xml" %>
	<%@ taglib prefix="fmt" uri="http://java.sun.com/jstl/fmt" %>
	<%@ taglib prefix="sql" uri="http://java.sun.com/jstl/sql" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head><title> Hello</title></head>
<body>

<form action="get.jsp?value=Moederborden" method="post">
<%
try{
    test t = new test();
    String content = t.readUrl("http://145.24.222.229:8123/Service/Service1.svc/Moederborden?zoekwoord=intel");
    int content2 = t.er(content);
    out.println("java file result = ");
    out.println(content2);
    for(int i = 0; i < content2; i++){
    	String tit = t.ep(content, i);
    	String nwe;
    	String id = t.getId(content, i);

    	if(tit.length() > 50){
    		nwe = tit.substring(0,50)+"...";
    		%><br>
    		<input type="radio" name="Moederborden" value="<%=id %>"><%
    	}else{
    		nwe = tit;
    		%><br>
        	<input type="radio" name="Moederborden" value="<%=id %>"><%
    	}
    	
    	out.println(nwe);
    }
    }catch(Exception ex){}

%>
<hr>
<input type="submit" value="Send">
</form>
<br>
<span style="color:red"> Hello </span>
<input type="Button" value="Hello"> </input>
</body>
</html>