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
String url = "http://145.24.222.229:8123/Service/Service1.svc/" + type+  "?zoekwoord=intel";
getspecs get = new getspecs();
String json = get.readUrl(url);
int length = get.er(json);
String value = null;
for(int i = 0; i < length; i++){
	value = get.ep(json, i, item);
	if(value != null){
		out.println(value);
		break;
	}
}
if(get.beschrijvinglength(value) != 0){
	out.println("<br>HI!");
}
%>
</body>
</html>