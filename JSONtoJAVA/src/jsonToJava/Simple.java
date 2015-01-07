package jsonToJava;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class Simple {
	public static void main (String[] args){
		JSONObject obj = null;
		try {
			obj = new JSONObject("{'beschrijving': [{'name': 'Thermisch vermogen', 'value': '220 W'},"
					+ " {'name': 'Geheugen kanaal ondersteuning', 'value': 'Dual'},"
					+ " {'name': 'Ondersteunde geheugen types', 'value': 'DDR3-SDRAM'},"
					+ " {'name': 'Ingebouwde grafische adapter', 'value': 'N'}, "
					+ "{'name': 'Processor socket', 'value': 'Socket AM3+'}, "
					+ "{'name': 'Processor-productieproces', 'value': '32 nm'},"
					+ " {'name': 'Geinstalleerde processorcache', 'value': '8 MB'},"
					+ " {'name': 'Processormodel', 'value': 'FX 9370'},"
					+ " {'name': 'L3 cache', 'value': '8 MB'},"
					+ " {'name': 'Processorfamilie', 'value': 'AMD FX'},"
					+ " {'name': 'Aantal processorkernen', 'value': '8'},"
					+ " {'name': 'Processor aantal threads', 'value': '8'}, "
					+ "{'name': 'Turbo-frequentie (max)', 'value': '4.7 GHz'},"
					+ " {'name': 'Processor operating modes', 'value': '64-bit'},"
					+ " {'name': 'Kloksnelheid processor', 'value': '4.4 GHz'},"
					+ " {'name': 'Box', 'value': 'Y'},"
					+ " {'name': 'AMD Virtualization Technology', 'value': 'Y'},"
					+ " {'name': 'AMD HyperTransport Technology', 'value': 'Y'},"
					+ " {'name': 'Component voor', 'value': 'PC'}],"
					+ " 'price': '205,99',"
					+ " 'description': '[KenmerkenThermisch vermogen: 220 WGeheugen kanaal ondersteuning: DualOndersteunde geheugen types: DDR3-SDRAMIngebouwde grafische adapter: NProcessor socket: Socket AM3+Processor-productieproces: 32 Geinstalleerde processorcache: 8 MBProcessormodel: FX 9370L3 cache: 8 MBProcessorfamilie: AMD FXAantal processorkernen: 8Processor aantal threads: 8Turbo-frequentie (max): 4.7 GHzProcessor operating modes: 64-bitKloksnelheid processor: 4.4 GHzBox: YAMD Virtualization Technology: YAMD HyperTransport Technology: YComponent voor: PC]',"
					+ " 'specs': [{'name': u'Gewicht', 'value': u'70 g'},"
					+ " {'name': 'Afmetingen inclusief verpakking', 'value': '12 x 8 x 3 cm (lxbxh)'},"
					+ " {'name': 'Artikelnummer', 'value': 'FD9370FHHKWOF'},"
					+ " {'name': 'EAN', 'value': '0730143303644'}],"
					+ " 'Title': 'CPU FX9370 X8 4.4Ghz 8MB AM3+ 220 watt'}");
			} catch (JSONException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		JSONArray beschrijving = null;
		JSONObject hi = null;
		try {
			beschrijving = obj.getJSONArray("beschrijving");
		} catch (JSONException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		System.out.println("------------------------------------------");
		System.out.println("Print alle values in de Beschrijving array");
		System.out.println("------------------------------------------");
		
		
		
		/**
		 * this uses REGEX to search for an EXACT occurrence of the word PROCESSOR,
		 * it searches in both NAME and VALUE fields of the 'beschrijvingen' array.
		 */
		
		
		/*
		 * Jacco, jij kan dus je IF statement veranderen door zo'n loop, zodat je code 'fout' proof is.
		 */
		
		String searchval = "220"; //Search value to be set.
		try {
			Pattern pattern = Pattern.compile("\\b"+ searchval + "\\b", Pattern.CASE_INSENSITIVE);
			for(int i = 0; i < beschrijving.length(); i ++){
				JSONObject test = beschrijving.getJSONObject(i);
				Matcher matcher = pattern.matcher(test.getString("name"));
				Matcher matchernam = pattern.matcher(test.getString("value"));
				if(matcher.find()){	
					System.out.println(searchval + " found in NAME");
				}
				if(matchernam.find()){
					System.out.println(searchval + " found in VALUE");
				}
				
				System.out.println("Name   =    " + test.getString("name"));
				System.out.println("Value    =    " + test.getString("value"));
			}
		} catch (JSONException e){
			e.printStackTrace();
		}
	}
	
}
