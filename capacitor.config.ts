import type { CapacitorConfig } from "@capacitor/cli";

const config: CapacitorConfig = {
  appId: "com.example.app",
  appName: "geosense",
  webDir: "out",
  bundledWebRuntime: false,
  server: {
    hostname: "localhost",
    cleartext: true,
    androidScheme: "http",
    allowNavigation: [
      "http://192.168.51.44:6000/*",
      "http://192.168.51.44:5500/*",
      "http://172.16.44.60:6000/*",
      "http://landslide.lalithadithyan.online/*",
    ],
  },
};

export default config;
