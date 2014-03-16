package com.jjp.passwd;

import org.apache.commons.lang3.StringUtils;

public class Passwd {
	 static void p(String s){
		System.out.println(s);
	}
	static void p(int n){
		for(int i=0;i<n;i++) System.out.println();
	}
	static void pc(String s,int len){
		System.out.println(StringUtils.center(s, len));
	}
public static void main (String args[]){
if (args.length == 0){
	pc("welcome !!!!",100);
	pc("to coder7dc's passwd program",100);
	p(4);
	
	p("Please enter password");
}
else p("this is in else");
}
}
