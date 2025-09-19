export const paginatorTemplate = `
  RowsPerPageDropdown
  CurrentPageReport
  FirstPageLink
  PrevPageLink
  PageLinks
  NextPageLink
  LastPageLink
`;

// export const rowsPerPageOptions = [10, 15, 20, 25];
export const rowsPerPageOptions = [1, 2, 3];

export const baseProps = {
  dataKey: "id",
  rowsPerPageOptions,
  rows: rowsPerPageOptions[0],
  paginatorTemplate,
  paginatorPosition: "both",
};
