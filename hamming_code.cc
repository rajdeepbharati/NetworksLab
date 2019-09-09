/**
 * Author: Rajdeep Bharati
 * 
 * Program to get a 4-bit dataword and required parity from
 * stdin and generate corresponding (7-bit) hamming code.
 */

#include <iostream>
#include <string>
using namespace std;

string generateCodeWord(string ps1, string ps2, string ps4, string p1,
                        string p2, string p4, string dw, int requiredParity)
{
    int ps1Count1 = 0, ps2Count1 = 0, ps4Count1 = 0;

    for (char &c : ps1)
    {
        if (c == '1')
            ps1Count1++;
    }
    if (ps1Count1 % 2 == 0)
        p1 = to_string(requiredParity);
    else
        p1 = to_string(!requiredParity);

    for (char &c : ps2)
    {
        if (c == '1')
            ps2Count1++;
    }
    if (ps2Count1 % 2 == 0)
        p2 = to_string(requiredParity);
    else
        p2 = to_string(!requiredParity);

    for (char &c : ps4)
    {
        if (c == '1')
            ps4Count1++;
    }
    if (ps4Count1 % 2 == 0)
        p4 = to_string(requiredParity);
    else
        p4 = to_string(!requiredParity);

    string codeword;
    codeword.push_back(dw.at(0));
    codeword.push_back(dw.at(1));
    codeword.push_back(dw.at(2));
    codeword.push_back(p4.at(0));
    codeword.push_back(dw.at(3));
    codeword.push_back(p2.at(0));
    codeword.push_back(p1.at(0));
    return codeword;
}

int main()
{
    string dataWord;    // 4-bit dataword
    int requiredParity; // odd (1) or even (0) parity
    cout << "Enter a 4-bit dataword: ";
    cin >> dataWord;
    if (dataWord.length() != 4)
    {
        cerr << "Please enter a 4-bit dataword" << endl;
        return EXIT_FAILURE;
    }
    for (char &c : dataWord)
    {
        if (c != '1' && c != '0')
        {
            cerr << "Please enter a binary dataword" << endl;
            return EXIT_FAILURE;
        }
    }
    cout << "Enter parity (0 for even, 1 for odd): ";
    cin >> requiredParity;
    if (requiredParity != 0 && requiredParity != 1)
    {
        cerr << "Please enter a boolean (0 or 1) parity" << endl;
        return EXIT_FAILURE;
    }
    string p1, p2, p4;
    string ps1 = p1 + dataWord[3] + dataWord[2] + dataWord[0];
    string ps2 = p2 + dataWord[3] + dataWord[1] + dataWord[0];
    string ps4 = p4 + dataWord[2] + dataWord[1] + dataWord[0];

    string hammingCode = generateCodeWord(ps1, ps2, ps4, p1, p2, p4, dataWord, requiredParity);
    cout << "Hamming Code: " << hammingCode << endl;

    return 0;
}
