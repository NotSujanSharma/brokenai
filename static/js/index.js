document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("myForm");

  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = new FormData(form);
    const url = form.getAttribute("data-submit-url");
    try {
      const response = await fetch(url, {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(
          `Server responded with ${response.status}: ${await response.text()}`
        );
      }

      const result = await response.json();

      document.getElementById("response").innerText =
        result.message || result.error;
    } catch (error) {
      console.error("Fetch error:", error);
      document.getElementById("response").innerText =
        "An error occurred. Please try again.";
    }
  });
});
