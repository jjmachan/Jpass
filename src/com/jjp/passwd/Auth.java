package com.jjp.passwd;

import java.io.IOException;
import java.io.InputStream;


public class Auth {
	public boolean auth(String s)
	throws IOException
	{
final InputStream is = this.getClass().getResourceAsStream("com.jjp.passwd.pass.txt");
		System.out.println("this is what the real pass is : "+is);
		 if (is.equals("jithin")) return true;
		else return false;
	}
	
}
