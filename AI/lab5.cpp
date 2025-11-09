// ==================== CHATBOT DEMONSTRATION ROADMAP ====================
// 1. INTRODUCTION:
//   -> This is a simple rule-based chatbot in C++.
//   -> It uses string normalization, conditional logic, and .find() to simulate conversation.

// 2. GREETING TEST:
//   You: hello
//   Chatbot: Hello! How can I assist you today?

// 3. PERSONALITY TEST:
//   You: how are you
//   Chatbot: I'm just a computer program, but I'm doing well. How can I help you?

// 4. NAME EXTRACTION:
//   You: my name is Dipanshu
//   Chatbot: Nice to meet you, Dipanshu!

// 5. POLITENESS CHECK:
//   You: thank you
//   Chatbot: You're welcome! Always happy to help.

// 6. EMOTION HANDLING:
//   You: I am sad
//   Chatbot: I'm sorry to hear that. I hope things get better soon.

// 7. NEGATIVE INPUT:
//   You: you are stupid
//   Chatbot: That's not very nice. Let's stay positive, okay?

// 8. FUN RESPONSE:
//   You: tell me a joke
//   Chatbot: Why did the computer get cold? Because it left its Windows open.

// 9. TIME QUERY:
//   You: time
//   Chatbot: The current time is (system time printed).

// 10. EXIT CHAT:
//   You: bye
//   Chatbot: Goodbye! If you have more questions, feel free to ask later.
// =======================================================================

#include <iostream>
#include <string>
#include <algorithm>
#include <ctime>
using namespace std;

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

        if (input == "hello" || input == "bello" || input == "hi" || input == "hey" || input == "hii" || input == "hello there") {
            cout << "Chatbot: Hello! How can I assist you today?" << endl;
        }
        else if (input == "how are you" || input == "how r you" || input == "how r u" || input == "how arrr you") {
            cout << "Chatbot: I'm just a computer program, but I'm doing well. How can I help you?" << endl;
        }
        else if (input.find("name") != string::npos) {
            cout << "Chatbot: I don't have a personal name, you can call me Chatbot." << endl;
        }
        else if (input.find("my name is") != string::npos) {
            string name = input.substr(input.find("my name is") + 10);
            while (!name.empty() && name.front() == ' ') name.erase(name.begin());
            cout << "Chatbot: Nice to meet you, " << name << "!" << endl;
        }
        else if (input.find("thank") != string::npos) {
            cout << "Chatbot: You're welcome! Always happy to help." << endl;
        }
        else if (input.find("sorry") != string::npos) {
            cout << "Chatbot: No worries! It's okay." << endl;
        }
        else if (input.find("dont help") != string::npos || input.find("i dont want to talk") != string::npos) {
            cout << "Chatbot: Alright, I'll stay quiet for now. Type 'resume' when you want to talk again." << endl;
            string resume;
            while (true) {
                getline(cin, resume);
                resume = normalize(resume);
                if (resume == "resume") {
                    cout << "Chatbot: Welcome back! Let's continue chatting." << endl;
                    break;
                }
            }
        }
        else if (input.find("good") != string::npos || input.find("nice") != string::npos) {
            cout << "Chatbot: Glad to hear that." << endl;
        }
        else if (input.find("bad") != string::npos || input.find("sad") != string::npos) {
            cout << "Chatbot: I'm sorry to hear that. I hope things get better soon." << endl;
        }
        else if (input.find("stupid") != string::npos || input.find("idiot") != string::npos || input.find("i hate you") != string::npos) {
            cout << "Chatbot: That's not very nice. Let's stay positive, okay?" << endl;
            cout << "Chatbot: Do you want to continue talking? (yes/no)" << endl;
            string reply;
            cout << "You: ";
            getline(cin, reply);
            reply = normalize(reply);
            if (reply == "no") {
                cout << "Chatbot: If you don't wanna talk, I can tell you a joke." << endl;
                cout << "Chatbot: Why did the computer go to therapy? Because it had too many bytes of sadness." << endl;
            } 
            else if (reply == "yes") {
                cout << "Chatbot: Great! Let's keep chatting then." << endl;
            } 
            else {
                cout << "Chatbot: Hmm, I didn't quite get that - but I'll take it as a yes." << endl;
            }
        }
        else if (input.find("time") != string::npos) {
            time_t now = time(0);
            cout << "Chatbot: The current time is " << ctime(&now);
        }
        else if (input.find("joke") != string::npos) {
            cout << "Chatbot: Why did the computer get cold? Because it left its Windows open." << endl;
        }
        else if (input.find("help") != string::npos) {
            cout << "Chatbot: I can chat, tell jokes, or answer greetings. Try saying 'tell me a joke' or 'how are you'." << endl;
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
