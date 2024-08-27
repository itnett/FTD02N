import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Text("Hei, verden!")
                .font(.largeTitle)
                .padding()

            Button(action: {
                print("Knappen ble trykket!")
            }) {
                Text("Klikk meg")
            }
            .padding()
            .background(Color.blue)
            .foregroundColor(.white)
            .cornerRadius(8)
        }
    }
}