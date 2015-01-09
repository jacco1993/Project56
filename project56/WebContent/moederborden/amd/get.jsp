<%@ page language="java" contentType="text/html; charset=US-ASCII"
    pageEncoding="US-ASCII"%>
    <%@page import="project56.getspecs" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=US-ASCII">
<title>GETjsp</title>
</head>
<body>
U heeft het volgende item geselecteerd: <br>
<%
String item =  request.getParameter("Moederborden");
String type = request.getParameter("value");
out.println(item);
String url = "http://145.24.222.229:8123/Service/Service1.svc/" + type+  "?zoekwoord=amd";
String json = getspecs.readUrl(url);
int length = getspecs.er(json);
String value = null;
for(int i = 0; i < length; i++){
	value = getspecs.ep(json, i, item);
	if(value != null){
		break;
	}
}
%>
<h1><%=getspecs.gettitle(value) %></h1><%
if(getspecs.beschrijvinglength(value) != 0){
	int size = getspecs.beschrijvinglength(value);
	%>
	<h2> Beschrijving</h2> 
	<hr>
	<table>
	<%
	for(int x =0; x < size; x++){
		%><tr><td><%=getspecs.beschrijvingname(value, x)
		%></td><td><%=getspecs.beschrijvingvalue(value, x)%></td></tr>
		<%
	}
	%></table><% 
}else{
	%><h2> Beschrijving (Textueel)</h2>
	<hr>
	<%=getspecs.getdescription(value)%>
	<%
}
%>
<h2> Productspecificaties</h2>
<hr>
<table>
<%
int specsize = getspecs.specslength(value); 
for(int s = 0; s < specsize; s++){
	%><tr><td><%=getspecs.specsname(value, s) %>
	</td><td><%=getspecs.specsvalue(value, s) %></td></tr>
	<%
}
%>
</table>
</body>
</html>