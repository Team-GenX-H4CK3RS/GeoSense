"use client";

export type LanguageItem = [string, string];

export type TranslationResult = {
  audio: string;
  result: string;
  lang: string;
};

export default function useTranslate() {
  const fetchData = async (url, options = {}) => {
    const response = await fetch("http://10.11.159.177:5500" + url, options);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  };

  const getLanguages = async () => {
    return await fetchData(`/languages`);
  };

  const translate = async (langCode: string, text: string) => {
    const response = await fetch(`${"http://10.11.159.177:5500"}/translate`, {
      body: JSON.stringify({ text, lang_code: langCode }),
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    });
    if (response.status === 500) return await translate(langCode, text);
    return (await response.json()) as TranslationResult;
  };

  return {
    getLanguages,
    translate,
  };
}
