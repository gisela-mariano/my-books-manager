import { getFileByLanguage } from "@core/i18n/getFileByLanguage"
import { createI18n } from "vue-i18n"
// import { useUserPreference } from "@providers/composables/useUserPreference"

const locale = getFileByLanguage("pt-BR")
// const { language } = useUserPreference()
// TODO: Adicionar preferencias de idioma do usuário
const language = {
  get: () => "pt",
}

type MessageSchema = typeof locale

export const i18n = createI18n<[MessageSchema], "pt" | "es" | "en">({
  legacy: false,
  locale: language.get(),
  fallbackLocale: "en",
  globalInjection: true,
  messages: {
    pt: getFileByLanguage("pt-BR"),
    es: getFileByLanguage("es-ES"),
    en: getFileByLanguage("en-US"),
  },
  numberFormats: {
    pt: {
      currency: {
        style: "decimal",
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
      },
      integer: {
        style: "decimal",
        minimumFractionDigits: 0,
        maximumFractionDigits: 0,
      },
      decimal: {
        style: "decimal",
        minimumFractionDigits: 0,
        maximumFractionDigits: 2,
      },
      percent: {
        style: "percent",
        useGrouping: false,
      },
    },
    en: {
      currency: {
        style: "decimal",
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
      },
      decimal: {
        style: "decimal",
        minimumFractionDigits: 0,
        maximumFractionDigits: 2,
      },
      integer: {
        style: "decimal",
        minimumFractionDigits: 0,
        maximumFractionDigits: 0,
      },
      percent: {
        style: "percent",
        useGrouping: false,
      },
    },
    es: {
      currency: {
        style: "decimal",
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
      },
      decimal: {
        style: "decimal",
        minimumFractionDigits: 0,
        maximumFractionDigits: 2,
      },
      integer: {
        style: "decimal",
        minimumFractionDigits: 0,
        maximumFractionDigits: 0,
      },
      percent: {
        style: "percent",
        useGrouping: false,
      },
    },
  },
})
