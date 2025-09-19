import { I18nKeys } from "@common/types";
import { Ref, computed } from "vue";
import { useI18n } from "vue-i18n";

type Options = {
  overWriteKey?: string;
};

export const useDataViewReportTemplate = (total: Ref<number>, options?: Options) => {
  const { t } = useI18n();

  const baseKey = `${I18nKeys.GLOBAL}.components.dataView.paginator`;
  const { overWriteKey } = options ?? {};

  const report = computed(() => {
    const recordKey = overWriteKey ?? `${baseKey}.record`;

    return `
      ${t(`${baseKey}.showingFrom`)} {first}-{last}
      ${t(`${baseKey}.of`)}
      ${t(recordKey, total.value)}
    `;
  });

  return {
    report,
  };
};
