package project56;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;

import org.json.*;
public class test {
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
	
	public static String ep(String str, int x) throws Exception{
		JSONArray json = new JSONArray(str);
		
		JSONObject current = json.getJSONObject(x);
		String title = current.getString("titles");
		return title;
	}
	public static String getId(String string, int s) throws Exception{
		JSONArray jsonar = new JSONArray(string);
		JSONObject currentone = jsonar.getJSONObject(s);
		JSONObject idobj = currentone.getJSONObject("_id");
		Object id = idobj.get("_increment");
		return id.toString();
	}
}
