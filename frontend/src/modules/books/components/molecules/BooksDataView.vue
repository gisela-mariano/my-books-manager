<template>
  <DataView
    :value="books"
    :layout="layout"
    v-bind="baseProps"
    paginator
    :currentPageReportTemplate="report"
  >
    <template #header>
      <div class="flex justify-end">
        <SelectButton class="button" v-model="layout" :options="options" :allowEmpty="false">
          <template #option="{ option }">
            <i
              v-tooltip.top="{
                value: t(`${I18nKeys.BOOKS}.components.booksDataView.header.buttons.${option}`),
                class: 'default-tooltip',
              }"
              :class="[option === DataViewLayout.LIST ? 'pi pi-bars' : 'pi pi-table']"
            />
          </template>
        </SelectButton>
      </div>
    </template>

    <template #list="slotProps">
      <div class="cont-cards flex flex-col">
        <CardBook
          v-for="(book, index) in slotProps.items"
          :key="index"
          :book="book"
          :layout="DataViewLayout.LIST"
        />
      </div>
    </template>

    <template #grid="slotProps">
      <div class="cont-cards layout-grid">
        <CardBook v-for="(book, index) in slotProps.items" :key="index" :book="book" />
      </div>
    </template>
  </DataView>
</template>

<script setup lang="ts">
import { I18nKeys } from "@common/types";
import { useDataViewReportTemplate } from "@global/composables";
import { DataViewLayout } from "@global/types";
import { baseProps } from "@global/utils";
import CardBook from "@modules/books/components/atoms/CardBook.vue";
import { SelectButton } from "primevue";
import { computed, ref } from "vue";
import { useI18n } from "vue-i18n";
import { books as dataBooks } from "./books";

const { t } = useI18n();

const options = [DataViewLayout.GRID, DataViewLayout.LIST];
const books = ref(dataBooks);
const totalBooks = computed(() => books.value.length);
const layout = ref(DataViewLayout.GRID);

const { report } = useDataViewReportTemplate(totalBooks);
</script>

<style scoped lang="scss">
i,
.button,
:deep(.button span) {
  cursor: pointer;
}

.cont-cards {
  overflow: hidden;
  padding: prem(16);
  gap: prem(8);
}

.cont-cards.layout-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
}
</style>
