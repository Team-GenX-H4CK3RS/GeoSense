"use client";

export default function Settings() {
  return (
    <form
      className="p-4 flex flex-col space-y-2 select-none"
      onSubmit={(e) => {
        e.preventDefault();
        const fd = new FormData(e.currentTarget);
        localStorage.setItem("app-server-url", fd.get("serverUrl") as string);
      }}
    >
      <div className="flex items-center gap-2">
        <p className="text-2xl font-bold">Settings</p>
        <div className="flex-grow"></div>
        <button className="bg-teal-600 text-white px-4 py-1 rounded-lg font-semibold">
          Apply
        </button>
      </div>
      <hr />
      <div className="flex flex-col items-stretch mt-2">
        <label className="flex flex-col items-stretch px-2 py-1">
          <p className="font-semibold">Server URL</p>
          <input
            className="appearance-none px-3 py-1 rounded-lg border-2 border-slate-300 focus:outline-teal-600 disabled:border-transparent disabled:bg-slate-200 transition"
            name="serverUrl"
          />
        </label>
      </div>
    </form>
  );
}
