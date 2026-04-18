const tradePanels = document.querySelectorAll(".trade-panel");

tradePanels.forEach((panel) => {
  const tabs = panel.querySelectorAll(".tab");
  const tabPanels = panel.querySelectorAll(".tab-panel");
  const buyAmount = panel.querySelector("#buy-amount");
  const buyTotal = panel.querySelector("#buy-total");
  const marketPrice = Number(panel.dataset.marketPrice || "0");

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      const next = tab.dataset.tab;
      tabs.forEach((item) => item.classList.toggle("active", item === tab));
      tabPanels.forEach((item) => {
        item.classList.toggle("active", item.dataset.panel === next);
      });
    });
  });

  if (buyAmount && buyTotal) {
    const updateBuyTotal = () => {
      const total = Number(buyAmount.value) * marketPrice;
      buyTotal.textContent = `₩${total.toLocaleString("ko-KR")}`;
    };

    buyAmount.addEventListener("input", updateBuyTotal);
    updateBuyTotal();
  }
});
