function showSequenceDiagram() {
  document.getElementById('content').innerHTML =

 `
    <h1 class="text-2xl font-bold mb-4">Sequence Diagram</h1>
    <div class="mermaid">
      sequenceDiagram
      participant A as User
      participant B as Learning Platform
      participant C as Math Module
      A->>B: Request for Math Lesson
      B->>C: Fetch Lesson Data
      C->>B: Provide Lesson Data
      B->>A: Display Lesson
    </div>
  `;
  mermaid.init();
}