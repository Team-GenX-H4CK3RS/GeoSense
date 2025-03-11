import { useState } from "react";
//import useServerData from "./useServerData";
//http://landslide.lalithadithyan.online/phone/req/<lat>/<lon>
export default function usePrediction() {
  const [status, setStatus] = useState<string>();
  const [severity, setSeverity] = useState<number>();
  const [date, setDate] = useState<string>();
  //const serverData = useServerData();
  const pingStatus = () => {
    const data = { status: "success", payload: { sev: 3, date: "2025-02-27" } }; // await serverData.lpa.checkStatus(lat, lon);
    setStatus(data.status);
    if (data.status === "error") return;
    setSeverity(data.payload.sev);
    setDate(data.payload.date);
  };
  const getTextFromSeverity = () => {
    return ["None", "Yellow", "Orange", "Orange Red", "Red", "Severe Red"][
      severity
    ];
  };
  const getClassNameFromSeverity = () => {
    return [
      "bg-green-600",
      "bg-yellow-600",
      "bg-orange-600",
      "bg-orange-700",
      "bg-red-600",
      "bg-red-800",
    ][severity];
  };
  const start = () => {
    setInterval(async () => {
      await pingStatus();
    }, 5000);
  };
  return {
    status,
    severity,
    date,
    start,
    pingStatus,
    getTextFromSeverity,
    getClassNameFromSeverity,
  };
}
