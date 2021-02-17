package com.zhlc;

import org.apache.log4j.Logger;

import java.io.*;
import java.util.Scanner;


public class log4APIUsing {
private static final Logger log = Logger.getLogger(log4APIUsing.class);

    public static void main(String[] args) throws IOException {

        // Debug log output;
        String debugLog = "Debug log Details . . .";
        log.debug("Debug :\n" + "\t" + debugLog);

        // Configurating MySql;
        String[] arguments = new String[5];
        File f1 = new File("password.txt");
        if (!f1.isFile()) {
            String pythonFilePath = System.getProperty("user.dir") + "\\EPS.py ";
            System.out.println(pythonFilePath);
            arguments[0] = "python";
            arguments[1] = pythonFilePath;
            Scanner scanner = new Scanner(System.in);
            System.out.println("Input your MySql host address like 192.168.85.100 or host name: ");
            String mySqlAddress = scanner.nextLine();
            arguments[2] = mySqlAddress;
            System.out.println("Input your MySql user's name: ");
            String mySqlUserName = scanner.nextLine();
            arguments[3] = mySqlUserName;
            System.out.println("Input your MySql password: ");
            String mySqlPassword = scanner.nextLine();
            arguments[4] = mySqlPassword;
            f1.createNewFile();
            BufferedWriter input = new BufferedWriter(new FileWriter(f1));
            for (int i=0; i<5; i++) {
                input.write(arguments[i] + "\r\n");
            }
            input.flush();
            input.close();
        } else {
            InputStreamReader isr = new InputStreamReader(new FileInputStream(f1), "utf-8");
            BufferedReader br = new BufferedReader(isr);
            for (int i=0; i<5; i++) {
                arguments[i] = br.readLine();
            }
            br.close();
        }
//        String mySqlAddress = "namenode";
//        String mySqlUserName = "root";
//        String mySqlPassword = "Summer@2020";
//        String mySqlDataBase = "test";

//        StringJoiner sj = new StringJoiner("\" \"", " \"", "\" ");
//        sj.add(mySqlAddress);
//        sj.add(mySqlUserName);
//        sj.add(mySqlPassword);
//        sj.add(mySqlDataBase);
//
//        String pythonFilePath = System.getProperty("user.dir") + "\\EPS.py ";
//
//        // Calling Python script through the CMD;
//        String cmd="python " + pythonFilePath + sj.toString();
//        String[] arguments = new String[] {"python",
//                pythonFilePath,
//                mySqlAddress,
//                mySqlUserName,
//                mySqlPassword,
//                mySqlDataBase
//        };
        try{
//            Process p = Runti
//            me.getRuntime().exec(cmd);
            Process p = Runtime.getRuntime().exec(arguments);
            InputStream is = p.getErrorStream();            InputStreamReader isr = new InputStreamReader(is);
            BufferedReader br = new BufferedReader(isr);
            String line = null;
            System.out.println("Calling Python Script . . ");
            while((line = br.readLine())!=null){
                System.out.println("<ERROR>");
                System.out.println(line);
                System.out.println("</ERROR>");
                int exitValue = p.waitFor();
                System.out.println("Process exitValue="+exitValue);
            }
            System.out.println("\nEnd");

//            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream(),"utf-8"));
//            String line = null;
//            while ((line = in.readLine()) != null) {
//                System.out.println(line);
//            }
//            in.close();
//            //java代码中的process.waitFor()返回值为0表示我们调用python脚本成功，
//            //返回值为1表示调用python脚本失败，这和我们通常意义上见到的0与1定义正好相反
//            int re = p.waitFor();
//            System.out.println(re);

            // 以下是注释掉的参数使用：
//            InputStream fis = p.getInputStream();
//            InputStreamReader isr = new InputStreamReader(fis);
//            BufferedReader br = new BufferedReader(isr);
//            String line = null;
//            while ((line = br.readLine()) != null) {
//                System.out.println(line);
//            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

    }
}
