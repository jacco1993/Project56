package project56;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;

import org.json.JSONArray;
import org.json.JSONObject;

public class getspecs {
	public static String readUrl(String urlString) throws Exception {
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
	public static int er(String str) throws Exception {
		JSONArray json = new JSONArray(str);
		int i = 0;
		while(i < json.length()){
			JSONObject json1 = json.getJSONObject(i);
			i+=1;
		}
		return json.length();
		
	}
	public static String ep(String str, int x, String value) throws Exception{
		JSONArray json = new JSONArray(str);
		
		JSONObject current = json.getJSONObject(x);
		JSONObject idobj = current.getJSONObject("_id");
		Object id = idobj.get("_increment");
		String ids = id.toString();
		if(ids.equals(value)){
			return current.toString();
		}
		return null;
	}
	
	public static int beschrijvinglength(String str) throws Exception{
		JSONObject json = new JSONObject(str);
		JSONArray beschr = null;
		int beschrijvinglengte = 0;
		if(!json.get("beschrijving").equals(null)){
			beschr = json.getJSONArray("beschrijving");
			beschrijvinglengte = beschr.length();
		}
		return beschrijvinglengte;
	}
	
	public static String beschrijvingname(String str, int x) throws Exception{
		JSONObject all = new JSONObject(str);
		JSONArray beschrijving = all.getJSONArray("beschrijving");
		JSONObject json = beschrijving.getJSONObject(x);
		String name = json.getString("name");
		
		return name;
		
	}
	public static String beschrijvingvalue(String str, int x) throws Exception{
		JSONObject all = new JSONObject(str);
		JSONArray beschrijving = all.getJSONArray("beschrijving");
		JSONObject json = beschrijving.getJSONObject(x);
		String value = json.getString("value");
		return value;
		
	}
	
	public static String specsname(String str, int x) throws Exception{
		JSONObject all = new JSONObject(str);
		JSONArray specs = all.getJSONArray("specs");
		JSONObject json = specs.getJSONObject(x);
		String name = json.getString("name");
		return name;
	}
	public static String specsvalue(String str, int x) throws Exception{
		JSONObject all = new JSONObject(str);
		JSONArray specs = all.getJSONArray("specs");
		JSONObject json = specs.getJSONObject(x);
		String name = json.getString("value");
		return name;
	}
	public static int specslength(String str) throws Exception{
		JSONObject json = new JSONObject(str);
		JSONArray specs = json.getJSONArray("specs");
		int specslengte = specs.length();
		return specslengte;
	}
	
	public static String gettitle(String str) throws Exception{
		JSONObject json = new JSONObject(str);
		String title = json.getString("titles");
		return title;
	}
	
	public static String getdescription(String str) throws Exception{
		JSONObject json = new JSONObject(str);
		String description = json.getString("description");
		return description;
	}
}
