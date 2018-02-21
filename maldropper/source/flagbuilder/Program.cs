using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace flagbuilder
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Random r = new Random(0xE45EC7F);
            StringBuilder sb = new StringBuilder();
            sb.Append("easyctf{");
            for (int i = 0; i < 6; ++i)
                sb.Append(r.Next());
            sb.Append("}");

            string flag = sb.ToString();

            Console.WriteLine("Flag created!");
        }
    }
}
