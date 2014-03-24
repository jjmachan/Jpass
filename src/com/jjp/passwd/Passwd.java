package com.jjp.passwd;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Properties;

import org.apache.commons.lang3.StringUtils;

public class Passwd {
	public static void p(String s){
		System.out.println(s);
	}
	  static void p(int j) {
		 System.out.println(j);
	 }
	  static void pl(int n){
		for(int i=0;i<n;i++) System.out.println();
	}
	static void pc(String s,int len){
		System.out.println(StringUtils.center(s, len));
	}
public static void main (String args[]) throws IOException{
if (args.length == 0){
	pc("welcome !!!!",100);
	pc("to coder7dc's passwd program",100);
	pl(4);
	p("Please enter password");
}
else { for(int i=0;i<args.length;i++)
	{
		if(args[i].equals("-s")){
			p("proceed to sign in");
			i++;
			InputStream is =
				Passwd.class.getClassLoader().getResourceAsStream("Passwd/src/com.jjp.passwd/pass.txt");
			System.out.println("is "+is);
			String result = getStringFromInputStream(is);
			
			System.out.println("this is what the real pass is : "+result);
			p(" this is your pass : "+args[i]);
			final String passInString = args[i];
			if (passInString.equals("jithin")) p("pass verifid");
			else p("pass wrough");
			break ;
		}
		else if (args[i].equals("-h")) p("will display help");
		else if (args[i].equals("-c")) p("will change your password");
		else p ("please enter the correct option. Try -h for help");
	}
}
}
private static String getStringFromInputStream(InputStream is) {

		BufferedReader br = null;
		StringBuilder sb = new StringBuilder();
 
		String line;
		try {
 
			br = new BufferedReader(new InputStreamReader(is));
			while ((line = br.readLine()) != null) {
				sb.append(line);
			}
 
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (br != null) {
				try {
					br.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
 
		return sb.toString();
 
	}
 
}

