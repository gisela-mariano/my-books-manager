type Locale = { [key: string]: any }

export const getFileByLanguage = (language: "pt-BR" | "es-ES" | "en-US") => {
  const currentLanguageFilesContent = importAllFiles(language) as string[]

  let locale: Locale = {} as Locale

  // imports local locales
  currentLanguageFilesContent.forEach((file: any) => {
    locale = { ...locale, ...file }
  })

  return locale
}

const importAllFiles = (language: "pt-BR" | "es-ES" | "en-US"): string[] => {
  const files = import.meta.glob("../../**/*.json", { eager: true })
  const filesContent = Object.entries(files)
    .filter(([key]) => key.includes(language))
    .map(([, mod]) => (mod as any).default ?? mod)
  return filesContent
}
