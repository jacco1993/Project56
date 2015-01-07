package jsonToJava;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.text.ParseException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class Extended {
	private static String readUrl(String urlString) throws Exception {
		BufferedReader reader = null;
		try {
			URL url = new URL(urlString);
			reader = new BufferedReader(new InputStreamReader(url.openStream()));
			StringBuffer buffer = new StringBuffer();
			int read;
			char[] chars = new char[1024];
			while ((read = reader.read(chars)) != -1)
				buffer.append(chars, 0, read); 

			return buffer.toString();
		} finally {
			if (reader != null)
				reader.close();
		}
	}


	public static void main(String[] args) throws Exception{
		String Search = "http://145.24.222.229:8123/Service/Service1.svc/Moederborden?zoekwoord=";
		Search = Search + "INTEL";
		System.out.println(Search);
		String json = readUrl(Search);
		Moederbord(json);
	}
	
	/*
	 * Above uses reader to get all the JSON From the URL.
	 * URL is being created by Search + a key word entered in line 41.
	 * ----------
	 * Below is the search for MOEDERBORD 
	 * Using Pattern and Matcher to find the exact match on price
	 * in this case we search (searchval) for '255,99'.
	 * 
	 * From the string we recieve from readUrl we create a JSONArray
	 * We calculate the amount of JSONObjects in that array and loop through it
	 * If that matcher finds a match we break out of the loop and end the programm
	 * If not we continue to break up the JSONObject into smaller chunks
	 * getting each Key and Value,
	 * or each JSONArray within the JSONOBject (in example line 80)
	 */
	/**
	 * Making the Matcher find exact value can be done like so:
	 * @searchval <b>String</b> used to set where the matcher will be looking for 
	 * @EXAMPLE Pattern pattern = Pattern.compile("\\b" + searchval + "\\b", Pattern.CASE_INSENSITIVE);  <u style="color:green">for more info:</u><a href="http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html"> look here</a> </br>
	 * 			Matcher matcher = pattern.matcher(<i>JSONOBJECT</i>.getString("name")); <br>
	 * 			<span style="color:green">Now you will be looking for AMD in a JSONObjects Name</span>
	 * @param json
	 * @param searchval = AMD
	 * @throws JSONException
	 */
	
	private static void Moederbord(String json) throws JSONException{
		String searchval = "225,99";
		Pattern pattern = Pattern.compile("\\b" + searchval + "\\b", Pattern.CASE_INSENSITIVE);
		try{
			JSONArray jsonobj = new JSONArray(json);
			System.out.println("length of Array = " + jsonobj.length());
			for(int i = 0; i <jsonobj.length(); i ++){
				JSONObject first = jsonobj.getJSONObject(i);
				Matcher prijs = pattern.matcher(first.getString("price"));
				if(prijs.find()){
					System.out.println(first);
					break;
				}
				String test = first.getString("Title");
				try{
					if(first.getJSONArray("beschrijving") != null){
						JSONArray beschrijving = first.getJSONArray("beschrijving");
						for(int x = 0; x < beschrijving.length(); x++){
							JSONObject name = beschrijving.getJSONObject(x);
							//System.out.println(x + " name        =" + name.getString("name"));
							//System.out.println(x + " value        =" + name.getString("value"));
						}
					}else{
						System.out.println("BESCHRIJVING = NULL");
					}
				}catch(Exception e){
					System.out.println("NULL");
				}
				String description = first.getString("description");
				try{
					JSONArray specs = first.getJSONArray("specs");
					for(int specssize = 0; specssize < specs.length(); specssize++){
						JSONObject spec = specs.getJSONObject(specssize);
						//System.out.println(specssize + " name          = " + spec.getString("name"));
						//System.out.println(specssize + " value         = " + spec.getString("value"));
					}
				}catch(Exception e){
					System.out.println("ERROR ON LINE 76");
				}
				System.out.println("Title           = " + test);
				System.out.println("Price           = " + first.getString("price"));
				System.out.println("description     = " + description);
				System.out.println("---------Finished----------");
				if(i != jsonobj.length() -1){
					System.out.println();
				}
			}
		}finally{
			;
		}
	}
}
