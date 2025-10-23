#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Helper function to convert string to lowercase and remove extra spaces
string normalize(string s) {
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    while (!s.empty() && s.front() == ' ') s.erase(s.begin());
    while (!s.empty() && s.back() == ' ') s.pop_back();
    return s;
}

int main() {
    string input;
    cout << "Chatbot: Hello! I am your assistant Chatbot." << endl;
    cout << "Type 'bye' to exit the chat." << endl;

    while (true) {
        cout << "You: ";
        getline(cin, input);
        input = normalize(input);

        if (input == "hello" || input == "hi" || input == "hey" || input == "hii" || input == "hello there") {
            cout << "Chatbot: Hello! How can I assist you today?" << endl;
        }
        else if (input == "how are you" || input == "how r you" || input == "how r u" || input == "how arrr you") {
            cout << "Chatbot: I'm just a computer program, but I'm doing well. How can I help you?" << endl;
        }
        else if (input.find("name") != string::npos) {
            cout << "Chatbot: I don't have a personal name, you can call me Chatbot." << endl;
        }
        else if (input.find("my name is") != string::npos) {
            string name = input.substr(11);
            cout << "Chatbot: Nice to meet you, " << name << "!" << endl;
        }
        else if (input.find("thank") != string::npos) {
            cout << "Chatbot: You're welcome! Always happy to help." << endl;
        }
        else if (input.find("sorry") != string::npos) {
            cout << "Chatbot: No worries! It’s okay." << endl;
        }
        else if (input.find("dont help") != string::npos || input.find("i dont want to talk") != string::npos) {
            cout << "Chatbot: Alright, I’ll stay quiet for now. Take care!" << endl;
        }
        else if (input.find("good") != string::npos || input.find("nice") != string::npos) {
            cout << "Chatbot: Glad to hear that!" << endl;
        }
        else if (input.find("bad") != string::npos || input.find("sad") != string::npos) {
            cout << "Chatbot: I'm sorry to hear that. I hope things get better soon." << endl;
        }
        else if (input.find("stupid") != string::npos || input.find("idiot") != string::npos || input.find("i hate you") != string::npos) {
            cout << "Chatbot: That's not very nice 😞. Let's stay positive, okay?" << endl;
            cout << "Chatbot: Do you want to continue talking? (yes/no)" << endl;

            string reply;
            cout << "You: ";
            getline(cin, reply);
            reply = normalize(reply);

            if (reply == "no") {
                cout << "Chatbot: If you don't wanna talk, I can tell you a joke!" << endl;
                cout << "Chatbot: Why did the computer go to therapy? Because it had too many 'bytes' of sadness 😂" << endl;
            } 
            else if (reply == "yes") {
                cout << "Chatbot: Great! Let's keep chatting then 😄" << endl;
            } 
            else {
                cout << "Chatbot: Hmm, I didn’t quite get that — but I’ll take it as a yes 😅" << endl;
            }
        }
        else if (input == "bye" || input == "exit" || input == "quit") {
            cout << "Chatbot: Goodbye! If you have more questions, feel free to ask later." << endl;
            break;
        }
        else {
            cout << "Chatbot: Sorry, I didn't understand that. Could you please rephrase?" << endl;
        }
    }

    return 0;
}
