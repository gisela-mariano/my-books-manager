import Tooltip from "primevue/tooltip";
import { DirectiveBinding, VNode } from "vue";

interface ExtendedHTMLElement extends HTMLElement {
  $_ptooltipClass?: string;
  $_ptooltipValue?: string;
  $_ptooltipId?: string;
  $_ptooltipModifiers?: Record<string, boolean>;
  $_ptooltipDisabled?: boolean;
  $_ptooltipEscape?: boolean;
  $_ptooltipFitContent?: boolean;
  $_ptooltipZIndex?: number;
}

const vCustomTooltip = {
  ...Tooltip,

  beforeMount(el: ExtendedHTMLElement, binding: DirectiveBinding, vnode: VNode) {
    if (Tooltip.beforeMount) {
      Tooltip.beforeMount(el, binding, vnode, null);
    }

    el.$_ptooltipClass = "default-tooltip";
    el.$_ptooltipValue = el.innerText || "";
  },

  updated(el: ExtendedHTMLElement) {
    const tooltipElement = document.getElementById(el.$_ptooltipId!);
    if (tooltipElement) {
      const tooltipTextElement = tooltipElement.querySelector(".p-tooltip-text") as HTMLElement;
      if (tooltipTextElement) {
        tooltipTextElement.innerHTML = el.innerText;
      }
      tooltipElement.classList.add(el.$_ptooltipClass!);
    }
  },

  unmounted(el: ExtendedHTMLElement, binding: DirectiveBinding, vnode: VNode) {
    if (Tooltip.unmounted) {
      Tooltip.unmounted(el, binding, vnode, null);
    }

    const tooltipElement = document.getElementById(el.$_ptooltipId!);
    if (tooltipElement) {
      tooltipElement.classList.remove(el.$_ptooltipClass!);
    }
  },
};

export default vCustomTooltip;
